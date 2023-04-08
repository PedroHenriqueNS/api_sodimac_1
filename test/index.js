const express = require('express');
const request = require('request-promise');

const app = express();
const PORT = process.env.PORT || 5000
const API = '2a50240573146b75b8976c85642e62ca'

// const baseUrl = `http://api.scraperapi.com?api_key=${process.env.API_KEY}&autoparse=true`
const baseUrl = `http://api.scraperapi.com?api_key=${API}&autoparse=true&`

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to Sodimac Scraper API')
})

// GET Product Details
app.get('/product/:productId', async (req, res) => {
    const { productId } = req.params;

    try {
        // const response = await request(`${baseUrl}&url=https://www.sodimac.com.br/sodimac-br/product/${productId}/`)
        const response = await request(`https://www.sodimac.com.br/sodimac-br/product/${productId}/`)

        const data = JSON.parse(response)

        res.json(response)
    } catch (error) {
        res.json(error)
    }
})

app.listen(PORT, () => console.log(`Server runing on port "${PORT}"`))