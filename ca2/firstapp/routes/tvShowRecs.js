/*
    tvShowRecs.js -- Router for the tvShowRecs
*/
const express = require('express');
const router = express.Router();

const {Configuration, OpenAIApi } = require('openai');

const ChatGPT = require('../models/ChatGPT');
const configuration = new Configuration({
    apiKey: process.env.OPENAI_APIKEY,
})
const openai = new OpenAIApi(configuration);

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
        next()
    } else {
        res.redirect('/login')
    }
}

router.get('/tvShowRecs', isLoggedIn, async (req, res, ) => {
    ChatGPT.findOne().sort({date:-1})
        .then(function(doc) {
            console.log(doc);
            res.render('tvShowRecs', {dialogue : doc});
        });
});


router.post('/tvShowRecs',
    isLoggedIn,
    async (req, res, ) => {
        const prompt = req.body.question + ", give me a TV show recommendation and a brief summary of it";
        const response = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: prompt,
            max_tokens: 2048,
            temperature: 1,
        });

        const answer = response.data.choices[0].text;

        const conversation = new ChatGPT (
            {
                date: new Date(),
                prompt: prompt,
                response: response.data.choices[0].text.trim(),
                userId: req.user._id
            })
        await conversation.save();
        res.redirect('/tvShowRecs')
    });

module.exports = router;
