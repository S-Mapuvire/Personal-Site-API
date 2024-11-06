const express = require('express')
const router = express.Router()

const mongodb = require('mongodb');
const uri = process.env.MONGO_URI;

router.get('/:id', async(req, res)=>{
    try {
        const data = await getEntries(req.params.id)
        res.status(200).json(data)
    } catch (error) {
        res.status(500).json({error})
    }
})

async function accessDB(db){
    const client = await mongodb.MongoClient.connect(uri);
    if(db == 0){
        return client.db('Scrapbook').collection('Tags');
    }
    else if(db == 1){
        return client.db('Scrapbook').collection('Velcro');
    }
}

async function getEntries(mode) {
    const scrapbook = await accessDB(mode);
    // explicit casting of id because otherwise it sends it as a string
    const tags = (await scrapbook.find({}).toArray());
    return tags;
}

module.exports = router
