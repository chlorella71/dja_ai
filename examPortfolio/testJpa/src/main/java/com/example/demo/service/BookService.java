package com.example.demo.service;

import com.example.demo.entity.Book;
import com.example.demo.exception.NotFoundException;
import com.example.demo.repository.BookRepository;
import lombok.AllArgsConstructor;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Service
public class BookService {

    private final BookRepository bookRepository;

    public ResponseEntity<Book> createBook(Book book) {
        try {
            Book saved = bookRepository.save(book);
            return ResponseEntity.ok(saved);
        } catch (DataIntegrityViolationException e) {
            throw new IllegalArgumentException("잘못된 도서 정보입니다.");
        } catch (Exception e) {
            throw new RuntimeException("도서 저장중 알수없는 오류 발생");
        }
    }

    public ResponseEntity<List<Book>> getBooks() {
        List<Book> books = bookRepository.findAll();
        return ResponseEntity.status(HttpStatus.OK).body(books);
    }

    public ResponseEntity<Book> updateBook(Long id, Book updatedBook) {
        Book book = bookRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("해당 도서를 찾을 수 없습니다."));

        book.setTitle(updatedBook.getTitle());
        book.setAuthor(updatedBook.getAuthor());
        book.setPublisher(updatedBook.getPublisher());
        book.setPrice(updatedBook.getPrice());

        Book saved = bookRepository.save(book);
        return ResponseEntity.ok(saved);
    }

    public ResponseEntity<Void> deleteBook(Long id) {
        Book book = bookRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("해당 도서를 찾을 수 없습니다."));

        bookRepository.delete(book);
        return ResponseEntity.noContent().build();
    }
}
