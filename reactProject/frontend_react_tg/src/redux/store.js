import { configureStore } from "@reduxjs/toolkit";
import auth from './authSlice'
import promotion from "./promotionSlice";
import region from "./regionSlice"
import product from "./productSlice"
import channel from "./channelSlice"
import category from "./categorySlice"
import datePage from './datePageSlice'
import subcategory from "./subcategorySlice"
import sales from "./salesSlice"
import salePost from "./salePostSlice"


const store = configureStore({
    reducer:{
        auth,
        promotion,
        region,
        product,
        channel,
        category,
        datePage,
        subcategory,
        sales,
        salePost,
    }
});

export default store;
