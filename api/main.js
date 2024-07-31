const express = require('express');
const router = express.Router();
const mongodb = require('mongodb');

router.get('/', (req, res)=>{
    console.log(`Recieved request to: ${req.url}, type: ${req.method}`);
    res.status(200).json({message: 'getting'})
})
router.post('/', (req, res)=>{
    if(!req.body.text){
        res.status(400)
        throw new Error("POST error - please add a text field")
    }
    else{
        console.log(`Recieved request to: ${req.url}, type: ${req.method}`);
        res.status(200).json({message: 'setting'})
    }
})
router.put('/:id', (req, res)=>{
    console.log(`Recieved request to: ${req.url}, type: ${req.method}`);
    res.status(200).json({message: `updating ${req.params.id}`})
})
router.delete('/:id', (req, res)=>{
    console.log(`Recieved request to: ${req.url}, type: ${req.method}`);
    res.status(200).json({message: `deleting ${req.params.id}`})
})

module.exports = router;