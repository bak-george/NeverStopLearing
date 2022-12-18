const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/shopApp')
    .then(() => {
        console.log("Connection Open")
    })
    .catch(err => {
        console.log("oh no error!!!")
        console.log(err)
    })

    const productSchema = new mongoose.Schema({
        name: {
            type: String, 
            required: true,
            maxlength: 20
        },
        price: {
            type: Number,
            required: true
        }, 
        onSale: { 
            type: Boolean,
            default: false
        }
    })

    productSchema.methods.greet = function () {
        console.log('hello!');
        console.log(`- from ${this.name}`);
    }

    const Product = mongoose.model('Product', productSchema);

    const findProduct = async () => {
        const foundProduct = await Product.findOne({name: 'Mountain Bike'});
        foundProduct.greet();
    }

    findProduct();
/* 
    const bike = new Product({name: 'Mountain Bike', price: 599, color: 'red'});
    bike.save()
    .then(data => {
        console.log("IT WORKED")
        console.log(data);
    })
    .catch(err => {
        console.log("oh no error")
        console.log(err)
    }) */