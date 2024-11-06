const express = require('express')
const router = express.Router()

const mongodb = require('mongodb');
const uri = process.env.MONGO_URI;

router.get('/', async(req, res)=>{
    try {
        const data = await getEntries()
        res.status(200).json(data)
    } catch (error) {
        res.status(500).json({error})
    }
})

async function accessDB(){
    const client = await mongodb.MongoClient.connect(uri);
    return client.db('Scrapbook').collection('Tags');
}

async function getEntries() {
    const scrapbook = await accessDB();
    // explicit casting of id because otherwise it sends it as a string
    const tags = (await scrapbook.find({}).toArray());
    return tags;
}

module.exports = router
