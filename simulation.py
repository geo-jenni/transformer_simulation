
import streamlit as st
import json
import pandas as pd
from datetime import datetime

# Load logic tree
with open("transformer_simulation_logic_tree.json", "r") as f:
    logic_tree = json.load(f)

# Initialize session state
if "stage_index" not in st.session_state:
    st.session_state.stage_index = 0
    st.session_state.score = 0
    st.session_state.log = []
    st.session_state.last_feedback = ""

st.title("🔧 Transformer Replacement Simulation")
st.markdown("Simulate the safe and correct procedure for changing a utility transformer on a distribution pole.")

# Simulation in progress
if st.session_state.stage_index < len(logic_tree):
    current = logic_tree[st.session_state.stage_index]
    st.header(f"Stage {current['stage']}: {current['title']}")
    st.write(current["question"])

    options = list(current["options"].keys())
    choice = st.radio("Choose your action:", options, key=f"choice_{st.session_state.stage_index}")

    if st.button("Submit"):
        result = current["options"][choice]["result"]
        delta = current["options"][choice]["score"]
        st.session_state.score += delta

        # Log action
        st.session_state.log.append({
            "timestamp": datetime.now().isoformat(),
            "stage": current["stage"],
            "title": current["title"],
            "choice": choice,
            "result": result,
            "score_change": delta,
            "total_score": st.session_state.score
        })

        # Store feedback and advance stage
        st.session_state.last_feedback = f"**{result}**  \\nScore Change: {delta}"

        st.session_state.stage_index += 1

# Show last feedback
if st.session_state.last_feedback:
    st.markdown(st.session_state.last_feedback)
    st.session_state.last_feedback = ""

# Simulation complete
if st.session_state.stage_index >= len(logic_tree):
    st.subheader("✅ Simulation Complete")
    st.write(f"**Final Score: {st.session_state.score} / {len(logic_tree) * 10}**")

    df = pd.DataFrame(st.session_state.log)
    st.dataframe(df)

    # Downloadable log
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Your Action Log", csv, "simulation_log.csv", "text/csv")

    if st.button("Restart Simulation"):
        st.session_state.stage_index = 0
        st.session_state.score = 0
        st.session_state.log = []
        st.session_state.last_feedback = ""
