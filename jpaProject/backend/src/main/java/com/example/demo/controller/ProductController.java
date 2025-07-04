package com.example.demo.controller;

import com.example.demo.entity.Product;
import com.example.demo.service.ProductService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Validated
@RestController
@RequiredArgsConstructor
@RequestMapping("/products")   // api지정
//@CrossOrigin(origins = "http://localhost:5173")
public class ProductController {

    private final ProductService productService;

    @PostMapping("/batch")
    public ResponseEntity<List<Product>> registerProducts(@RequestBody @Valid List<@Valid Product> products) {
        List<Product> savedList = productService.registerProducts(products);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedList);
    }

//    @GetMapping
//    public ResponseEntity<List<Product>> getProducts() {
//        return ResponseEntity.ok(productService.getProducts());
//    }

    @GetMapping
    public ResponseEntity<List<Product>> getProducts() {
        try {
            List<Product> list = productService.getProducts();
            System.out.println("조회된 상품 수: " + list.size());
            for (Product p : list) {
                System.out.println("상품: " + p.getName() + " | 가격: " + p.getPrice());
            }
            return ResponseEntity.ok(list);
        } catch (Exception e) {
            System.err.println("🔥 예외 발생:");
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }



    @PostMapping
    public ResponseEntity<Product> registerProduct(@RequestBody @Valid Product product) {
        if (product.getName() == null) {
            throw new IllegalArgumentException("상품명은 필수입니다.");
        }

        return ResponseEntity.ok(productService.registerProduct(product));
    }
}
