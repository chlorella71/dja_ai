package com.example.demo.service;

import com.example.demo.entity.Customer;
import com.example.demo.exception.CustomerAlreadyExistsException;
import com.example.demo.exception.NotFoundException;
import com.example.demo.repository.CustomerRepository;
import lombok.AllArgsConstructor;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Service
public class CustomerService {

    public CustomerRepository customerRepository;

    public ResponseEntity<Customer> createCustomer(Customer customer) {
        try {
            if (customerRepository.existsByEmail(customer.getEmail())) {
                throw new CustomerAlreadyExistsException("이미 존재하는 이메일입니다.");
            }
            Customer saved = customerRepository.save(customer);
            return ResponseEntity.ok(saved);
        } catch (DataIntegrityViolationException e) {
            throw new IllegalArgumentException("잘못된 고객 정보입니다.");
        } catch (Exception e) {
            throw new RuntimeException("고객 저장 중 알 수 없는 오류 발생");
        }
    }

    public ResponseEntity<List<Customer>> getCustomers() {
        List<Customer> customers = customerRepository.findAll();
        return ResponseEntity.status(HttpStatus.OK).body(customers);
    }

    public ResponseEntity<Customer> updateCustomer(Long id, Customer updatedCustomer) {
        Customer customer = customerRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("해당 고객을 찾을 수 없습니다."));

        customer.setName(updatedCustomer.getName());
        customer.setEmail(updatedCustomer.getEmail());
        customer.setAge(updatedCustomer.getAge());

        Customer saved = customerRepository.save(customer);
        return ResponseEntity.ok(saved);
    }

    public ResponseEntity<Void> deleteCustomer(Long id) {
        Customer customer = customerRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("해당 고객을 찾을 수 없습니다."));

        customerRepository.delete(customer);
        return ResponseEntity.noContent().build();
    }
}
