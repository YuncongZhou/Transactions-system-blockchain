const mqtt = require('mqtt')
// const client  = mqtt.connect('mqtt://test.mosquitto.org')
const client2  = mqtt.connect('mqtt://127.0.0.1:1883')


var mosca = require('mosca');

var ascoltatore = {
  //using ascoltatore
  type: 'mongo',
  url: 'mongodb://',
  pubsubCollection: 'ascoltatore2',
  mongo: {}
};

var settings = {
  port: 1602,
  // backend: ascoltatore
};

var server = new mosca.Server(settings);

server.on('clientConnected', function(client) {
    console.log('client connected', client.id);
});

// fired when a message is received
server.on('published', function(packet, client) {
  console.log('Published', packet.payload);
  console.log(packet);
  if (packet.topic === 'presence'){
    client2.publish('presence', packet.payload)
  }

});

server.on('ready', setup);

// fired when the mqtt server is ready
function setup() {
  console.log('Mosca server is up and running');
  const client2  = mqtt.connect('mqtt://127.0.0.1:1883')
}
