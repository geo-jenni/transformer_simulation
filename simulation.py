
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

st.title("🔧 Transformer Replacement Simulation")
st.markdown("Simulate the safe and correct procedure for changing a utility transformer on a distribution pole.")

# Get current stage
if st.session_state.stage_index < len(logic_tree):
    current = logic_tree[st.session_state.stage_index]
    st.header(f"Stage {current['stage']}: {current['title']}")
    st.write(current["question"])

    # Display options as radio buttons
    options = list(current["options"].keys())
    choice = st.radio("Choose your action:", options)

    if st.button("Submit"):
        result = current["options"][choice]["result"]
        delta = current["options"][choice]["score"]
        st.session_state.score += delta

        # Log the choice
        st.session_state.log.append({
            "timestamp": datetime.now().isoformat(),
            "stage": current["stage"],
            "title": current["title"],
            "choice": choice,
            "result": result,
            "score_change": delta,
            "total_score": st.session_state.score
        })

        # Feedback
        st.success(f"**{result}**  
Score Change: {delta}")
        st.session_state.stage_index += 1
        st.experimental_rerun()

else:
    st.subheader("✅ Simulation Complete")
    st.write(f"**Final Score: {st.session_state.score} / {len(logic_tree) * 10}**")

    df = pd.DataFrame(st.session_state.log)
    st.dataframe(df)

    # Download log
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Your Action Log", csv, "simulation_log.csv", "text/csv")

    if st.button("Restart Simulation"):
        st.session_state.stage_index = 0
        st.session_state.score = 0
        st.session_state.log = []
        st.experimental_rerun()
