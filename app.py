import os

import streamlit as st

from video_utils import save_clip, convert_time, merge_videos


def main():
    st.title('Aplikacioni i procesimit te videove')

    tab1, tab2 = st.tabs(["Prej Videot", "Bashko Videot"])

    with tab1:
        st.header("Prersi i videove")
        uploaded_file = st.file_uploader("Zgjedh videot", type=['mp4', 'avi', 'mov', 'mkv'])
        start_time = st.text_input("Sheno kohen e fillimit ne kete format (OO : MM : SS):")
        end_time = st.text_input("Sheno kohen e mbarimit ne kete format (OO : MM : SS):")

        if st.button('Prej Videon') and uploaded_file is not None:
            start_seconds = convert_time(start_time)
            end_seconds = convert_time(end_time)
            output_path = "output_clip.mp4"

            save_clip(uploaded_file, start_seconds, end_seconds, output_path)
            st.success('Videoja eshte prere ne menyre te sukseseshme.')
            st.video(output_path)
            with open(output_path, "rb") as file:
                st.download_button("Shkarko videon e prere", file, file_name=output_path, mime="video/mp4")

            os.remove(output_path)

    with tab2:
        st.header("Bashko Videot")
        uploaded_files = st.file_uploader("Selektoj videot per ti bashkuar", accept_multiple_files=True,
                                          type=['mp4', 'avi', 'mov', 'mkv'])

        if st.button('Bashko videot') and uploaded_files:
            output_path = "merged_video.mp4"

            merge_videos(uploaded_files, output_path)
            st.success('Videot jane bashkuar me sukses.')
            st.video(output_path)
            with open(output_path, "rb") as file:
                st.download_button("Shkarko videon e bashkuar", file, file_name=output_path, mime="video/mp4")

            os.remove(output_path)


if __name__ == "__main__":
    main()
