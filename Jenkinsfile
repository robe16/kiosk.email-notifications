echo "Running Build ID: ${env.BUILD_ID}"

String commit_id
String docker_volumes
String deployLogin
String docker_img_name
def docker_img

node {

    deleteDir()

    stage("parameters") {
        // Parameters passed through from the Jenkins Pipeline configuration
        string(defaultValue: 'https://github.com/robe16/kiosk.grandparent-message-board.git', description: 'GitHub URL for checking out project', name: 'githubUrl')
        string(defaultValue: 'message_board', description: 'Name of application for Docker image and container', name: 'appName')
        string(defaultValue: '8080', description: 'Port number for python application running within container', name: 'portApplication')
        string(defaultValue: '8080', description: 'Port number to map portApplication to', name: 'portMapped')
        string(defaultValue: '~/config/message_board/config.json', description: 'Location of config json file on host device', name: 'fileConfig')
        string(defaultValue: '~/config/message_board/google_client_secret.json', description: 'Location of Google Client Secret json file on host device', name: 'fileGoogleSecret')
        string(defaultValue: '~/config/message_board/sheets.googleapis.com-python-messageboard.json', description: 'Location of Google Oauth json file on host device', name: 'fileGoogleOauth')
        //
        build_args = ["--build-arg portApplication=${params.portApplication}"].join(" ")
        //
        docker_volumes = ["-v ${params.fileConfig}:/message_board/config/config.json",
                          "-v ${params.fileGoogleSecret}:/message_board/google/google_client_secret.json",
                          "-v ${params.fileGoogleOauth}:/message_board/google/credentials/google_client_secret.json"].join(" ")
        //
        deployLogin = "${params.deploymentUsername}@${params.deploymentServer}"
        //
    }

    if (params["deploymentServer"]!="*" && params["deploymentUsername"]!="*" && params["serverIp"]!="*") {

        stage("checkout") {
            git url: "${params.githubUrl}"
            sh "git rev-parse HEAD > .git/commit-id"
            commit_id = readFile('.git/commit-id').trim()
            echo "Git commit ID: ${commit_id}"
        }

        docker_img_name_commit = "${params.appName}:${commit_id}"
        docker_img_name_latest = "${params.appName}:latest"

        stage("build") {
            try {sh "docker image rm ${docker_img_name_latest}"} catch (error) {}
            sh "docker build -t ${docker_img_name_commit} ."
            sh "docker tag ${docker_img_name_commit} ${docker_img_name_latest}"
        }

        stage("deploy"){
            //
            String docker_img_tar = "docker_img.tar"
            //
            try {
                sh "rm ~/${docker_img_tar}"                                                                 // remove any old tar files from cicd server
            } catch(error) {
                echo "No ${docker_img_tar} file to remove."
            }
            sh "docker save -o ~/${docker_img_tar} ${docker_img_name_commit}"                               // create tar file of image
            sh "scp -v -o StrictHostKeyChecking=no ~/${docker_img_tar} ${deployLogin}:~"                    // xfer tar to deploy server
            sh "ssh -o StrictHostKeyChecking=no ${deployLogin} \"docker load -i ~/${docker_img_tar}\""      // load tar into deploy server registry
            sh "ssh -o StrictHostKeyChecking=no ${deployLogin} \"docker tag ${docker_img_name_commit} ${docker_img_name_latest}\""
            sh "ssh -o StrictHostKeyChecking=no ${deployLogin} \"rm ~/${docker_img_tar}\""                  // remove the tar file from deploy server
            sh "rm ~/${docker_img_tar}"                                                                     // remove the tar file from cicd server
            //
        }

        stage("start container"){
            sh "ssh ${deployLogin} \"docker rm -f ${params.appName} && echo \"container ${params.appName} removed\" || echo \"container ${params.appName} does not exist\"\""
            sh "ssh ${deployLogin} \"docker run -d ${docker_volumes} -p ${params.portMapped}:${params.portApplication} --name ${params.appName} ${docker_img_name_latest}\""
        }

    } else {
        echo "Build cancelled as required parameter values not provided by pipeline configuration"
    }

}