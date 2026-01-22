# biologics/vm.py

class StackVM:
    """
    Minimal stack-based virtual machine for BioLogics.

    Features:
    - Stack operations: PUSH_1, PUSH_2, ADD, SUB, MUL, DIV
    - PRINT instruction
    - Safe execution: no crashes on empty stack
    """

    def __init__(self):
        self.stack = []

    def execute(self, instruction):
        try:
            if instruction == "PUSH_1":
                self.stack.append(1)
            elif instruction == "PUSH_2":
                self.stack.append(2)
            elif instruction == "ADD":
                # Pop values safely, default to 0
                b = self.stack.pop() if self.stack else 0
                a = self.stack.pop() if self.stack else 0
                self.stack.append(a + b)
            elif instruction == "SUB":
                b = self.stack.pop() if self.stack else 0
                a = self.stack.pop() if self.stack else 0
                self.stack.append(a - b)
            elif instruction == "MUL":
                b = self.stack.pop() if self.stack else 0
                a = self.stack.pop() if self.stack else 0
                self.stack.append(a * b)
            elif instruction == "DIV":
                b = self.stack.pop() if self.stack else 0
                a = self.stack.pop() if self.stack else 0
                # Avoid division by zero
                self.stack.append(a / b if b != 0 else 0)
            elif instruction == "PRINT":
                if self.stack:
                    value = self.stack.pop()
                    print(f"[organism output] {value}")
                else:
                    print("[organism output] (stack empty)")
            else:
                # Unknown instruction: ignore
                print(f"[organism output] (ignored unknown instruction: {instruction})")

        except Exception as e:
            # Catch any unexpected error
            print(f"[organism output] (execution error: {e})")
