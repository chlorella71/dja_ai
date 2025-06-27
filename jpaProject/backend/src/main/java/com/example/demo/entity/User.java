package com.example.demo.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Table(name="users")
@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    private Long id;

    @NotBlank(message = "이름은 필수입니다.")
    @Size(max=80, message="이름은 80자 이하로 입력해주세요.")
    @Column(name="name")
    private String name;

    @NotNull(message="나이는 필수입니다.")
    @Min(value= 0, message="나이는 0 이상이어야 합니다.")
    @Max(value=150, message="나이는 150이하로 입력해주세요.")
    @Column(name="age")
    private Long age;

    @NotBlank(message="이메일은 필수입니다.")
    @Email(message ="유효한 이메일 주소를 입력해주세요.")
    @Size(max=80, message = "이메일은 80자 이하로 입력해주세요.")
    @Column(name="email")
    private String email;

    @Size(max=80, message = "도시는 100자 이하로 입력해주세요.")
    @Column(name="city")
    private String city;
}
