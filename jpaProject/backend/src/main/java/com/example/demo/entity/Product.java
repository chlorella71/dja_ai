package com.example.demo.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.PositiveOrZero;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Table(name="products")
@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    private Long id;

    @NotBlank(message="상품 이름은 필수입니다.")
    @Size(max = 80, message = "상품 이름은 80자 이하로 입력해주세요.")
    @Column(name="name", nullable = false)
    private String name;

    @Size(max = 80, message ="카테고리 이름은 80자 이하로 입력해주세요.")
    @Column(name="category", nullable = true)
    private String category;

    @Column(name="inStock")
    private boolean inStock;

    @PositiveOrZero(message="가격은 0이상이어야 합니다.")
    @Column(name="price")
    private Long price;
}
