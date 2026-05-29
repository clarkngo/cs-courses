# 1. Reset system_utilities.py back to its original buggy baseline state
cat << 'EOF' > system_utilities.py
# Bug 1: SyntaxError (Mismatched bracket/parenthesis formatting)
def print_items(items):
    for i in range(len(items)):
        print(items[i

# Bug 2: NameError (Variable typo tracking)
def circle_area(radius):
    return 3.14 * radius * radus

# Bug 3: ZeroDivisionError (Unhandled mathematical edge case)
def divide(a, b):
    return a / b

# Bug 4: Assignment syntax mismatch
def check_name(name):
    if name = "":
        return True
    return False

if __name__ == "__main__":
    print("Running Quality Controls...")
    try: print_items([1, 2, 3])
    except: pass
    try: print(circle_area(5))
    except: pass
    try: print(divide(10, 0))
    except: pass
    try: check_name("Clark")
    except: pass
EOF

# 2. Clear out historical artifact state files
rm -f eval_results.json debugging_report.md

# 3. Run the upgraded triage orchestrator
python agent_debugger.py

# 4. Evaluate the results
python eval_debugger.py