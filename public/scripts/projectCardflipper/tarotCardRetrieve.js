const mongodb = require('mongodb');
const uri = process.env.MONGO_URI;

async function accessDB () {
    const client = await mongodb.MongoClient.connect(uri);
    return client.db('Tarot').collection('Cards');
}

async function getEntry(cardNumber) {
    const card = await accessDB();
    const cardDetails = (await card.find({_id: cardNumber}).toArray());
    return cardDetails
}

// The maximum is exclusive and the minimum is inclusive
function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); 
}

function main (){
    const cardNumber = getRandomInt(0, 22);
    const cardDetails = getEntry(cardNumber)
    return cardDetails;
}

module.exports = {
    main
}