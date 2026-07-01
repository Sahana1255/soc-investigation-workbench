from collections import Counter

import pandas as pd
import streamlit as st


def iocs(iocs):

    st.subheader("🌐 IOC Explorer")

    counter = Counter()

    for ioc in iocs:

        counter[(ioc.type, ioc.value)] += 1

    rows = []

    for (ioc_type, value), count in counter.items():

        rows.append({

            "IOC Type": ioc_type,

            "Value": value,

            "Occurrences": count

        })

    st.dataframe(

        pd.DataFrame(rows),

        use_container_width=True,

        height=600

    )