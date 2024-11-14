#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
async function getChars () {
  const resp = await sendRequest(url);
  const characters = JSON.parse(resp.body).characters;
  for (const character of characters) {
    const characterResp = await sendRequest(character);
    const name = JSON.parse(characterResp.body).name;
    console.log(name);
  }
}

function sendRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, resp) {
      if (err) {
        reject(err);
      }
      resolve(resp);
    });
  });
}
getChars();
