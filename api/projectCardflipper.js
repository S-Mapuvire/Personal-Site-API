const express = require('express');
const router = express.Router();
const mongodb = require('mongodb');
const { main } = require('../public/scripts/projectCardflipper/tarotCardRetrieve')

//GET posts
router.get('/', async (req, res) => {
    const card = await main();
    res.status(200).json(card[0]);
    
    console.log(`Recieved request to: ${req.url}, type: ${req.method}`);
});

//POST posts
router.post('/', async (req, res) => {
    res.status(400);
    throw new Error("POST error - cannot POST to this server.");
});

//UPDATE posts
router.put('/:id', async (req, res) => {
    res.status(400);
    throw new Error("PUT error - cannot PUT to this server.");
})

//DELETE posts
router.delete('/:id', async (req, res) => {
    res.status(400);
    throw new Error("DELETE error - cannot delete from this server.");
})

module.exports = router;