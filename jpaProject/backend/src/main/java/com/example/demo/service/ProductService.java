package com.example.demo.service;

import com.example.demo.entity.Product;
import com.example.demo.repository.ProductRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductRepository productRepository;

    @Transactional
    public Product registerProduct(Product product) {
        if (product.getId() != null && productRepository.existsById(product.getId())) {
            throw new IllegalArgumentException("이미 존재하는 상품 Id입니다: "+ product.getId());
        }
        return productRepository.save(product);
    }

    public List<Product> registerProducts(List<Product> products) {
        List<Product> savedProducts = new ArrayList<>();
        for (Product product : products) {
            Product saved = registerProduct(product);
            savedProducts.add(saved);
        }
        return savedProducts;
    }

    public List<Product> getProducts() {
        return productRepository.findAll();
    }
}
