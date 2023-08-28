from doublyList import DoublyLL

# Criação de uma lista encadeada dupla
dll = DoublyLL()
dll.insertAtEnd(1)
dll.insertAtEnd(2)
dll.insertAtEnd(3)
dll.insertAtEnd(4)

print("Lista original:")
DoublyLL.print(dll)

# Deletar do começo
dll.deleteFromBeginning()
print("Lista após deletar do começo:")
DoublyLL.print(dll)

# Deletar do final
dll.deleteFromEnd()
print("Lista após deletar do final:")
DoublyLL.print(dll)

# Deletar de uma posição específica
dll.deleteAtPosition(1)
print("Lista após deletar na posição 1:")
DoublyLL.print(dll)
