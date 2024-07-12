try:
    from styles.style_plain import plain
    from styles.style_regular import regular
    from styles.style_json import json_
except ImportError as e:
    print(f"ImportError: {e}")

print(f"plain is callable: {callable(plain)}")
print(f"regular is callable: {callable(regular)}")
print(f"json_ is callable: {callable(json_)}")

