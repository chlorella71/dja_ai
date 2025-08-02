import React, { useMemo } from 'react';

const ProductDisplay = ({products, filterText}) => {
    const filteredProducts = useMemo(() =>{
        return products.filter(product=>product.name.includes(filterText))
    }, [products, filterText])
  return (
    <div>
      <h2>ShowDisplay</h2>
        {filteredProducts.map(p=><div key={p.id}>{p.name}</div>)}
    </div>
  );
}

export default ProductDisplay;
