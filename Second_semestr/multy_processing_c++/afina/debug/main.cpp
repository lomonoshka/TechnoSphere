#include <string>
#include <memory>
#include <iostream>


class Lru_cash_list {
    public:
        // LRU cache node
        struct lru_node {
            std::string key;
            std::string value;
            lru_node* prev;
            std::unique_ptr<lru_node> next;

            lru_node(std::string key_, std::string value_, lru_node* prev_, lru_node* next_)
            : key(key_),
              value(value_),
              prev(prev_),
              next(next_)
              {}

            lru_node() = default;
        };

    private:

        std::unique_ptr<lru_node> _lru_head = nullptr;

    public:
        // Insert new element to begining of lru list
        void push_front(const std::string &key, const std::string &value);

        //  Return pointer to the last element
        lru_node* back() const;

        //  Return pointer to the first element
        lru_node* front() const;

        // Delete last elements from lru list
        void pop_back();

        // Delete first elements from lru list
        void pop_front();

        //Erase element on reference
        void erase(lru_node* node);
        
        // Clear list
        void reset();

        void print() {
            auto tmp_node = front();
            while (tmp_node != nullptr) {
                std::cout << tmp_node->key << " " << tmp_node->value << std::endl;
                tmp_node = tmp_node->next.get();
            }
        }
};
#define PRINTL std::cout << __LINE__ << std::endl;

void Lru_cash_list::push_front(const std::string &key, const std::string &value)
{
    if (_lru_head == nullptr) {
        // _lru_head = std::make_unique<lru_node>(key, value, _lru_head, nullptr); c++14
        _lru_head = std::unique_ptr<lru_node>(new lru_node);
        _lru_head->key = key;
        _lru_head->value = value;
        _lru_head->prev = _lru_head.get();
    } else {
        // auto &new_node = _lru_head->prev->next;
        // _lru_head.reset(std::unique_ptr<lru_node>(new lru_node));
        // _lru_head->next=nullptr;
        // PRINTL;
        auto new_head = std::unique_ptr<lru_node>(new lru_node);
        // PRINTL;
        new_head->prev = _lru_head->prev;
        // PRINTL;
        new_head->next = std::move(_lru_head);
        // PRINTL;
        new_head->next->prev = new_head.get();
        // PRINTL;
        new_head->key = key;
        // PRINTL;
        new_head->value = value;
        // PRINTL;
        _lru_head = std::move(new_head);
    }
}

Lru_cash_list::lru_node* Lru_cash_list::back() const {
    return _lru_head->prev;
}

Lru_cash_list::lru_node* Lru_cash_list::front() const {
    return _lru_head.get();
}

void Lru_cash_list::pop_back() {
    auto &new_last_node = _lru_head->prev->prev;
    new_last_node->next = nullptr;
    _lru_head->prev = new_last_node;
}

void Lru_cash_list::pop_front() {
    auto &new_head = _lru_head->next;
    new_head->prev = _lru_head->prev;
    _lru_head = std::move(new_head);
}

void Lru_cash_list::erase(lru_node* node) {
    if (node == _lru_head.get()) {
        pop_front();
    } else if (node == _lru_head->prev) {
        pop_back();
    } else {
        node->next->prev = node->prev;
        node->prev->next = std::move(node->next);
        node = nullptr;
    }
}

void Lru_cash_list::reset() {
    _lru_head = nullptr;
}


int main() {
    Lru_cash_list l;
    for (int i = 0; i < 51; ++i) {
        l.push_front("keks" + std::to_string(i), "shmeks");
        std::cout << l.front()->key << " " << l.front()->value << " " << (bool)l.front()->next << (bool)l.front()->prev << std::endl; 
    }


    l.print();

    for (int i = 0; i < 10; ++i) {
        l.pop_front();
        l.pop_back();
    }
    std::cout << "reset" << std::endl;
    l.print();

    return 0;
}
