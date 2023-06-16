
'use strict';
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var chatgptSchema = Schema( {
    date: Date,
    prompt: String,
    response: String,
    userId: {type:ObjectId, ref:'user' }
});

module.exports = mongoose.model('ChatGPT', chatgptSchema);