#!/usr/bin/node

const get_request = require('request');

get_request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const action = JSON.parse(body).characters;
  exactOrder(action, 0);
});
const exactOrder = (action, x) => {
  if (x === action.length) return;
  get_request(action[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(action, x + 1);
  });
};
