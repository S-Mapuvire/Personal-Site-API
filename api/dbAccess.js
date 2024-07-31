const express = require('express');
const router = express.Router();
const mongodb = require('mongodb');

//GET posts
router.get('/', async (req, res) => {
    const posts = await loadPostsCollection();
    res.send(await posts.find({}).toArray());
    // res.status(200).json({
    //     message: 'getting'
    // })
});

//POST posts
router.post('/', async (req, res) => {
    const posts = await loadPostsCollection();
    await posts.insertOne({
        text: req.body.text,
        createdAt: new Date()
    });
    res.status(201).send();
    // res.status(200).json({
    //     message: 'setting'
    // })
});

//UPDATE posts
router.put('/:id', async (req, res) => {
    res.status(200).json({
        message: `updating ${req.params.id}`
    })
})

//DELETE posts
router.delete('/:id', async (req, res) => {
    const posts = await loadPostsCollection();
    await posts.deleteOne({ _id: new mongodb.ObjectId(req.params.id) });
    res.status(200).send();
    // res.status(200).json({
    //     message: `deleting ${req.params.id}`
    // })
})

const uri = "mongodb://user1:zwLw2o2g3aMFWAXH@ac-fxmu09j-shard-00-00.o6utkdl.mongodb.net:27017,ac-fxmu09j-shard-00-01.o6utkdl.mongodb.net:27017,ac-fxmu09j-shard-00-02.o6utkdl.mongodb.net:27017/?ssl=true&replicaSet=atlas-lx1p9k-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

async function loadPostsCollection () {
    const client = await mongodb.MongoClient.connect(uri);
    return client.db('MEVN').collection('posts');
}

module.exports = router;