from ArrayList import ArrayList

def main():
    print("Creating list...")
    lst = ArrayList() 
    
    print("\nAppending elements:")
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print(f"Length: {lst.length()}")  
    
    print("\nInserting 'd' at position 1:")
    lst.insert('d', 1)
    print(f"Element at index 1: {lst.get(1)}")  
    
    print("\nDeleting element at index 2:")
    print(f"Deleted: {lst.delete(2)}")  
    print(f"New length: {lst.length()}")  
    
    print("\nCloning list:")
    clone = lst.clone()
    clone.append('e')
    print(f"Original length: {lst.length()}") 
    print(f"Clone length: {clone.length()}")  
     
    print("\nReversing list:")
    lst.reverse()
    print(f"First element after reverse: {lst.get(0)}") 

    print("\nFinding first 'd':")
    print(f"Index: {lst.findFirst('d')}")  
    
   
    print("\nClearing list:")
    lst.clear()
    print(f"Length after clear: {lst.length()}")

if __name__ == "__main__":
    main()
