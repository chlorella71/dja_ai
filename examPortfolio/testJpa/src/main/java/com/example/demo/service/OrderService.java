package com.example.demo.service;

import com.example.demo.entity.Book;
import com.example.demo.entity.Customer;
import com.example.demo.entity.Order;
import com.example.demo.exception.NotFoundException;
import com.example.demo.repository.BookRepository;
import com.example.demo.repository.CustomerRepository;
import com.example.demo.repository.OrderRepository;
import lombok.AllArgsConstructor;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Service
public class OrderService {

    private final OrderRepository orderRepository;
    private final CustomerRepository customerRepository;
    private final BookRepository bookRepository;

    public ResponseEntity<Order> createOrder(Long customerId, Long bookId) {
        try {
            Customer customer = customerRepository.findById(customerId)
                    .orElseThrow(() -> new NotFoundException("고객을 찾을 수 없습니다."));

            Book book = bookRepository.findById(bookId)
                    .orElseThrow(() -> new NotFoundException("도서를 찾을 수 없습니다."));

            Order order = new Order();
            order.setCustomer(customer);
            order.setBook(book);

            Order saved = orderRepository.save(order);
            return ResponseEntity.ok(saved);
        } catch (DataIntegrityViolationException e) {
            throw new IllegalArgumentException("잘못된 주문 정보입니다.");
        } catch (Exception e) {
            throw new RuntimeException("주문 처리 중 오류가 발생했습니다.");
        }
    }

    public ResponseEntity<List<Order>> getOrders() {
        List<Order> orders = orderRepository.findAll();
        return ResponseEntity.status(HttpStatus.OK).body(orders);
    }

    public ResponseEntity<Void> deleteOrder(Long id) {
        Order order = orderRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("해당 주문을 찾을 수 없습니다."));

        orderRepository.delete(order);
        return ResponseEntity.noContent().build();
    }
}
