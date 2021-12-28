function changeActive(id){
    var body = document.body.id;
    var itemId = "item-" + body;
    var element = document.getElementById(itemId);
    // window.alert(element.textContent);
    element.classList.add("active");
}

window.onload = function (){
    var inputUsername = document.querySelector('#username');
    var btnJoin = document.querySelector('#btn-join')

    var username;
    var mapPeers = {};
    var webSocket;
    function webSocketOnMessage(event){
        var parsedData = JSON.parse(event.data);
        var peerUsername = parsedData['peer'];
        var action = parsedData['action'];

        if(username == peerUsername){
            return;
        }
        var receiver_channel_name = parsedData['message']['receiver_channel_name']

        if(Action == 'new-peer'){
            createOfferer(peerUsername,receiver_channel_name);
            return;
        }
        console.log('message:',message);

        if(action == 'new-offer'){
            var offer = parsedData['message']['sdp'];

            createAnswerer(offer,peerUsername,receiver_channel_name);

            return;
        }

        if (action == 'new-answer'){
            var answer = parsedData['message']['sdp'];

            var peer = mapPeers[peerUsername][0];

            peer.setRemoteDescription(answer);
            return;
        }
    }


    btnJoin.addEventListener('click', () => {
        username = inputUsername.value;
        console.log('username:',username);
        
        if(username == ''){
            return;
            }
        
        inputUsername.value = '';
        inputUsername.disabled = true;
        inputUsername.style.visibility = 'hidden';
        
        btnJoin.disabled = true;
        btnJoin.style.visibility = 'hidden';
        
        var labelUsername = document.querySelector('#label-username');
        labelUsername.innerHTML = username;

        var loc = window.location; //return object contain location

        var wsStart = 'ws://'; //it will specify that we are using web socket

        if(loc.protocol == 'https:'){
            wsStart = 'wss://';
        }

        var endPoint = wsStart + loc.host + loc.pathname;
        console.log('endPoint:',endPoint)

        webSocket = new WebSocket(endPoint); // new instance of chat consumer will be creqated for wach connection
        
        webSocket.addEventListener('open', (e) =>{
            console.log('connection opened');

            sendSignal('new-peer',{});

            var jsonStr = JSON.stringify({
                'message':'This is message'
            });
            webSocket.send(jsonStr);
        });
        webSocket.addEventListener('message',webSocketOnMessage);
        webSocket.addEventListener('close',(e) =>{
            console.log('connection closed');
        });      
        webSocket.addEventListener('error',(e) =>{
            console.log('error occured');
        });
    })

    var localStream = new MediaStream();


    const constraints = {
        'video':true,
        'audio':true
    };

    const localVideo = document.querySelector('#local-video');
    const btnToggleAudio = document.querySelector('#btn-toggle-audio');
    const btnToggleVideo = document.querySelector('#btn-toggle-video');



    var userMedia = navigator.mediaDevices.getUserMedia(constraints).then(stream =>{
        localStream = stream;
        localVideo.srcObject = localStream;
        localVideo.muted = true;

        var audioTracks = stream.getAudioTracks();
        var videoTracks = stream.getVideoTracks();

        audioTracks[0].enabled = true;
        videoTracks[0].enabled = true;

        btnToggleAudio.addEventListener('click', () => {
            audioTracks[0].enabled = !audioTracks[0].enabled;

            if(audioTracks[0].enabled){
                btnToggleAudio.innerHTML = 'Audio Mute';
                return;
            }
            btnToggleAudio.innerHTML = 'Audio Unmute';
        });

        btnToggleVideo.addEventListener('click', () => {
            videoTracks[0].enabled = !videoTracks[0].enabled;

            if(videoTracks[0].enabled){
                btnToggleVideo.innerHTML = 'Video off';
                return;
            }
            btnToggleVideo.innerHTML = 'Video on';
        });


    })
    .catch(error => {
        console.log('error',error);
    });

    function sendSignal(action,message){
        var jsonStr = JSON.stringify({
            'peer':username,
            'action':action,
            'message':message,
        });
        webSocket.send(jsonStr);

    }

    function createOfferer(peerUsername,receiver_channel_name){
        var peer = new RTCPeerConnection(null);

        addLocalTracks(peer);

        var dc = peer.createDataChannel('channel');
        dc.addEventListener('open',() =>{
            console.log('connection opend');
        });

        dc.addEventListener('message',dcOnMessage);
        var remoteVideo = createVideo(peerUsername);
        setOnTrack(peer,remoteVideo);

        mapPeers[peerUsername] = [peer,dc];
        //close connection if peer disconnect

        peer.addEventListener('iceconnectionstatechange',() => {
            var iceconnectionState = peer.iceConnectionState;

            if(iceconnectionState === 'failed' || iceconnectionState === 'disconnected' || iceconnectionState === 'closed'){
                delete mapPeers[peerUsername];
                if(iceconnectionState !='closed'){
                    peer.close();
                 }
                removeVideo(remoteVideo);
             }


        });
        peer.addEventListener('icecandidate',(event) => {
            if(event.candidate){
                console.log('New ice candidate:',JSON.stringify(peer.localDescription));

                return;
            }
            sendSignal('new-offer',{
                'sdp':peer.localDescription,
                'receiver_channel_name':receiver_channel_name
            });
        });
        peer.createOffer()
            .then(o => peer.setLocalDescription(o))
            .then(() => {
                console.log('local description set succefully.')
            });
    }

    function createAnswerer(offer,peerUsername,receiver_channel_name){
        var peer = new RTCPeerConnection(null);

        addLocalTracks(peer);

        // var dc = peer.createDataChannel('channel');
        // dc.addEventListener('open',() =>{
        //     console.log('connection opend');
        // });

        // dc.addEventListener('message',dcOnMessage);
        var remoteVideo = createVideo(peerUsername);
        setOnTrack(peer,remoteVideo);

        peer.addEventListener('datachannel', e => {
            peer.dc = e.channel;

            peer.dc.addEventListener('open',() =>{
                console.log('connection opend');
            });
    
            peer.dc.addEventListener('message',dcOnMessage);
            mapPeers[peerUsername] = [peer,peer.dc];
        });

        // mapPeers[peerUsername] = [peer,dc];
        //close connection if peer disconnect

        peer.addEventListener('iceconnectionstatechange',() => {
            var iceconnectionState = peer.iceConnectionState;

            if(iceconnectionState == 'failed' || iceconnectionState == 'disconnected' || iceconnectionState == 'closed'){
                delete mapPeers[peerUsername];
                if(iceconnectionState !='closed'){
                    peer.close();
                 }
                removeVideo(remoteVideo);
             }


        });
        peer.addEventListener('icecandidate',(event) => {
            if(event.candidate){
                console.log('New ice candidate:',JSON.stringify(peer.localDescription));

                return;
            }
            sendSignal('new-answer',{
                'sdp':peer.localDescription,
                'receiver_channel_name':receiver_channel_name
            });
        });
        peer.setRemoteDescription(offer)
            .then(() => {
                console.log('remote description set successfully for %s.',peerUsername);
                return peer.createAnswer();
            })
            .then(a => {
                console.log('answer created');

                peer.setLocalDescription(a);
            })

    }

    function addLocalTracks(peer){
        localStream.getTracks().forEach(track =>{
            peer.addTrack(track,localStream);
        });
        return
    }
    var messageList = document.querySelector('#msg-list')
    function dcOnMessage(event){
        var message = event.data;
        var li = document.createElement('li');
        li.appendChild(document.createTextNode(message));
        messageList.appendChild(li);
    }

    function createVideo(peerUsername){
        var videoContainer = document.querySelector('#video-container');

        var remoteVideo = document.createElement('video');

        remoteVideo.id = peerUsername + '-video';
        remoteVideo.autoplay = true;
        remoteVideo.playsInline = true;

        var videoWrapper = document.createElement('div');
        videoContainer.appendChild(videoWrapper);

        videoWrapper.appendChild(remoteVideo);
        return remoteVideo;
    }

    function setOnTrack(peer,remoteVideo){
        var remoteStream = new MediaStream();

        remoteVideo.srcObject = remoteStream;

        peer.addEventListener('track',async (event) => {
            remoteStream.addTrack(event.track,remoteStream);
        })
    }
    function removeVideo(video){
        var videoWrapper = video.parentNode;

        videoWrapper.parentNode.removeChilde(videoWrapper);
    }
}



    
// btnJoin.addEventListener('click', () => {
//    
// })


