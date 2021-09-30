const room_name = JSON.parse(document.getElementById('json-roomname').textContent);
const user_name = JSON.parse(document.getElementById('json-username').textContent);
const req_user_name = JSON.parse(document.getElementById('json-req-username').textContent);

document.getElementById('chat-message-input').focus()

var start = ''
if (window.location.protocol == 'https:') {
    start = 'wss'
}
else {
    start = 'ws'
}

console.log(start)
const endpoint = `${start}://${window.location.host}/${start}/${room_name}/`
console.log(endpoint)
var chat_socket = new ReconnectingWebSocket(endpoint)

chat_socket.onmessage = function (e) {
    console.log('On Message')
    var text_display = ''
    var data = JSON.parse(e.data)
    var user_message_name = data['username']
    var dt = new Date();
    let time = `${dt.getHours()}:${dt.getMinutes()}`
    var date = dateToYMD(dt)
    var date_time = `${date} ${time}`
    console.log(user_message_name)
    if (data.message) {
        if (req_user_name === user_message_name){
            text_display = `
            <div class="w-full flex justify-start">
                <div class="bg-gray-100 rounded px-5 py-2 my-2 text-gray-700 relative"
                     style="max-width: 300px;">
                     <strong><span class="block text-xs text-right">${user_message_name}</span></strong>
                    <span class="block">${data.message}</span>
                    <span class="block text-xs text-right">${date_time}</span>
                </div>
            </div>`
            document.getElementById('chat-messages').innerHTML += (text_display);
        }
        else{
            text_display = `
            <div class="w-full flex justify-end">
                <div class="bg-gray-100 rounded px-5 py-2 my-2 text-gray-700 relative"
                     style="max-width: 300px;">
                     <strong><span class="block text-xs text-right">${user_message_name}</span></strong>
                    <span class="block">${data.message}</span>
                    <span class="block text-xs text-left">${date_time}</span>
                </div>
            </div>
            `
            document.getElementById('chat-messages').innerHTML += (text_display);
        }
    } else {
        alert('Message is Empty!')
    }
}

chat_socket.onclose = function (e) {
    console.log('Closed')
}

document.getElementById('chat-message-submit').onclick = function (e) {
    const messageInputDom = document.getElementById('chat-message-input')
    const message = messageInputDom.value;

    chat_socket.send(JSON.stringify({
        'message': message,
        'username': user_name,
        'room': room_name
    }));
    messageInputDom.value = ''
}

document.getElementById('chat-message-input').addEventListener(
    'keyup', function (event) {
        if (event.code === 'Enter'){
            const messageInputDom = document.getElementById('chat-message-input')
            const message = messageInputDom.value;

            chat_socket.send(JSON.stringify({
                'message': message,
                'username': user_name,
                'room': room_name
            }));
            messageInputDom.value = ''
        }
    }
)

function dateToYMD(date) {
    var d = date.getDate()
    var m = date.getMonth() + 1
    var y = date.getFullYear()
    return '' + y + '-' + (m<=9 ? '0' + m : m) + '-' + (d <= 9 ? '0' + d : d)
}