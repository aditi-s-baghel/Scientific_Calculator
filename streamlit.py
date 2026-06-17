import streamlit as st
import math

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ScientificCalc",
    page_icon="⚛️",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.hero-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: #7c6ef7;
    text-transform: uppercase;
    border: 1px solid #7c6ef7;
    border-radius: 999px;
    padding: 0.25rem 0.85rem;
    margin-bottom: 1rem;
}
.hero-title {
    font-size: clamp(2rem, 6vw, 3.2rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #e8e8f0 30%, #7c6ef7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.4rem;
}
.hero-sub {
    font-size: 0.9rem;
    color: #6b6b80;
    font-weight: 400;
    letter-spacing: 0.02em;
}

/* ── Operation grid ── */
.op-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.65rem;
    margin: 1.8rem 0 1.2rem;
}
.op-btn {
    background: #13131f;
    border: 1px solid #1e1e30;
    border-radius: 12px;
    padding: 0.85rem 0.5rem;
    cursor: pointer;
    transition: all 0.18s ease;
    text-align: center;
    color: #c8c8d8;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    line-height: 1.4;
}
.op-btn:hover {
    background: #1a1a2e;
    border-color: #7c6ef7;
    color: #fff;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(124,110,247,0.15);
}
.op-btn.active {
    background: linear-gradient(135deg, #3d2f8f, #1e1260);
    border-color: #7c6ef7;
    color: #fff;
    box-shadow: 0 0 0 1px #7c6ef7, 0 4px 20px rgba(124,110,247,0.3);
}
.op-btn .op-icon {
    font-size: 1.35rem;
    display: block;
    margin-bottom: 0.2rem;
}
.op-btn .op-label {
    font-size: 0.72rem;
    color: inherit;
    opacity: 0.85;
}

/* ── Input panel ── */
.input-panel {
    background: #0f0f1a;
    border: 1px solid #1e1e30;
    border-radius: 16px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1rem;
}
.panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    color: #6b6b80;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* Number inputs */
div[data-testid="stNumberInput"] label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    color: #9898b0;
    font-weight: 400;
}
div[data-testid="stNumberInput"] input {
    background: #0a0a0f !important;
    border: 1px solid #2a2a42 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 0.9rem !important;
    transition: border-color 0.15s !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #7c6ef7 !important;
    box-shadow: 0 0 0 2px rgba(124,110,247,0.2) !important;
    outline: none !important;
}

/* ── Calculate button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #7c6ef7, #4f3fd4) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    padding: 0.75rem 1rem !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    transition: all 0.18s ease !important;
    box-shadow: 0 4px 24px rgba(124,110,247,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(124,110,247,0.5) !important;
    background: linear-gradient(135deg, #8d80f9, #6050e0) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, #0f1a2e, #0a1020);
    border: 1px solid #1a3060;
    border-radius: 16px;
    padding: 1.6rem;
    margin-top: 1rem;
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #7c6ef7, #00d4ff, transparent);
}
.result-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: #4a8ac4;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.result-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(1.6rem, 4vw, 2.4rem);
    font-weight: 600;
    color: #e8f4ff;
    word-break: break-all;
    line-height: 1.2;
}
.result-expr {
    font-size: 0.78rem;
    color: #4a8ac4;
    margin-top: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
}

/* Error card */
.error-card {
    background: #1a0a0a;
    border: 1px solid #5a1a1a;
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    margin-top: 1rem;
    color: #ff8080;
    font-size: 0.88rem;
}

/* ── History ── */
.history-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 0.65rem 0;
    border-bottom: 1px solid #13131f;
    font-size: 0.83rem;
}
.history-expr {
    color: #6b6b80;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
}
.history-val {
    color: #c8c8d8;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.88rem;
}
.history-title {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: #3a3a50;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 0.4rem;
}

/* Divider */
.divider {
    border: none;
    border-top: 1px solid #1a1a28;
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)


# ── Calculator logic ──────────────────────────────────────────────────────────
class Calculator:
    def add(self, a, b):        return a + b
    def subtract(self, a, b):   return a - b
    def multiply(self, a, b):   return a * b
    def divide(self, a, b):
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    def square(self, a):        return a ** 2
    def cube(self, a):          return a ** 3
    def sqrt(self, a):
        if a < 0: raise ValueError("Square root of a negative number is undefined")
        return math.sqrt(a)
    def power(self, a, b):      return a ** b
    def factorial(self, a):
        if a < 0:   raise ValueError("Factorial of negative numbers is undefined")
        if a != int(a): raise ValueError("Factorial requires a whole number")
        return math.factorial(int(a))
    def is_prime(self, a):
        n = int(a)
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True


calc = Calculator()

OPERATIONS = [
    ("➕", "Add",         "add",       True),
    ("➖", "Subtract",    "subtract",  True),
    ("✖️",  "Multiply",   "multiply",  True),
    ("➗", "Divide",      "divide",    True),
    ("²",  "Square",      "square",    False),
    ("³",  "Cube",        "cube",      False),
    ("√",  "Square Root", "sqrt",      False),
    ("^n", "Power",       "power",     True),
    ("!",  "Factorial",   "factorial", False),
    ("𝑝",  "Is Prime",   "is_prime",  False),
]

# ── Session state ─────────────────────────────────────────────────────────────
if "op" not in st.session_state:
    st.session_state.op = "add"
if "history" not in st.session_state:
    st.session_state.history = []

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-badge">⚛️ Scientific Calculator</span>
    <h1 class="hero-title">Compute Anything</h1>
    <p class="hero-sub">Ten operations · instant results · clean history</p>
</div>
""", unsafe_allow_html=True)

# ── Operation selector ────────────────────────────────────────────────────────
st.markdown('<div style="font-size:0.72rem;letter-spacing:0.12em;color:#3a3a50;text-transform:uppercase;font-family:\'JetBrains Mono\',monospace;margin-bottom:0.5rem;">SELECT OPERATION</div>', unsafe_allow_html=True)

cols = st.columns(5)
for idx, (icon, label, key, two_inputs) in enumerate(OPERATIONS):
    with cols[idx % 5]:
        is_active = st.session_state.op == key
        btn_class = "op-btn active" if is_active else "op-btn"
        # Use Streamlit button styled via CSS classes
        if st.button(f"{icon}\n{label}", key=f"btn_{key}", use_container_width=True):
            st.session_state.op = key
            st.rerun()

# Highlight active (visual pill via markdown — complementing button state)
active_op = next((o for o in OPERATIONS if o[2] == st.session_state.op), OPERATIONS[0])
icon, label, key, two_inputs = active_op

st.markdown(f"""
<div style="display:flex;align-items:center;gap:0.5rem;margin:0.8rem 0 1.2rem;padding:0.6rem 0.9rem;
            background:#13131f;border:1px solid #7c6ef7;border-radius:10px;
            font-size:0.82rem;color:#a898ff;font-family:'Space Grotesk',sans-serif;">
    <span style="font-size:1.1rem;">{icon}</span>
    <span>Operation: <strong style="color:#e8e8f0;">{label}</strong></span>
</div>
""", unsafe_allow_html=True)

# ── Input panel ───────────────────────────────────────────────────────────────
st.markdown('<div class="input-panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-label">INPUT VALUES</div>', unsafe_allow_html=True)

if two_inputs:
    c1, c2 = st.columns(2)
    with c1:
        a = st.number_input("First number (A)", value=0.0, format="%g", key="input_a")
    with c2:
        b = st.number_input("Second number (B)", value=0.0, format="%g", key="input_b")
else:
    a = st.number_input("Number", value=0.0, format="%g", key="input_a")
    b = None

st.markdown('</div>', unsafe_allow_html=True)

# ── Calculate ─────────────────────────────────────────────────────────────────
calc_btn = st.button("Calculate  →", use_container_width=True)

if calc_btn:
    try:
        fn = getattr(calc, key)
        if two_inputs:
            result = fn(a, b)
            expr   = f"{a} {icon} {b}"
        else:
            result = fn(a)
            expr   = f"{icon}({a})"

        # Format result
        if key == "is_prime":
            display = "Prime ✓" if result else "Not Prime ✗"
            color   = "#5bdf8a" if result else "#ff6b6b"
        elif isinstance(result, float):
            display = f"{result:,.10g}"
            color   = "#e8f4ff"
        else:
            display = f"{result:,}" if isinstance(result, int) else str(result)
            color   = "#e8f4ff"

        # Result card
        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">RESULT</div>
            <div class="result-value" style="color:{color};">{display}</div>
            <div class="result-expr">{expr} = {display}</div>
        </div>
        """, unsafe_allow_html=True)

        # Save to history
        st.session_state.history.insert(0, (expr, display))
        if len(st.session_state.history) > 10:
            st.session_state.history = st.session_state.history[:10]

    except (ZeroDivisionError, ValueError, OverflowError) as e:
        st.markdown(f"""
        <div class="error-card">
            ⚠️ &nbsp; <strong>Error:</strong> {e}
        </div>
        """, unsafe_allow_html=True)

# ── History ───────────────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    hcol1, hcol2 = st.columns([3, 1])
    with hcol1:
        st.markdown('<div class="history-title">Recent calculations</div>', unsafe_allow_html=True)
    with hcol2:
        if st.button("Clear", key="clear_hist"):
            st.session_state.history = []
            st.rerun()

    for expr, val in st.session_state.history:
        st.markdown(f"""
        <div class="history-item">
            <span class="history-expr">{expr}</span>
            <span class="history-val">{val}</span>
        </div>
        """, unsafe_allow_html=True)