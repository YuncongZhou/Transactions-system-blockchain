const mqtt = require('mqtt')
// const client  = mqtt.connect('mqtt://test.mosquitto.org')
const client  = mqtt.connect('mqtt://127.0.0.1:1602')

function delay(ms) {
  return new Promise(function (resolve, reject) {
      setTimeout(resolve, ms);
  });
}

function usingDelay1() {
  console.log('a');
  delay(1000)
  .then(() => {
      console.log('b');
  });
}

client.on('connect',  async () => {

  client.subscribe('presence')
  let time;
  for (let i = 0; i < 10; i++){
    time = new Date().getTime()
    client.publish('presence', time.toString())
  }

  for (let i = 0; i < 10; i++){
    time = new Date().getTime()
    await delay(2)
    client.publish('presence', time.toString())
  }
})

client.on('message',  (topic, message) => {
  // message is Buffer
  console.log(message.toString())
  // client.end()
})
