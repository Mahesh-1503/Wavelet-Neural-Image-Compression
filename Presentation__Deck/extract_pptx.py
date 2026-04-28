import zipfile
import xml.etree.ElementTree as ET
import sys
import re

def extract_text_from_pptx(pptx_path):
    try:
        with zipfile.ZipFile(pptx_path) as z:
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort(key=lambda x: int(re.search(r'slide(\d+)\.xml', x).group(1)))
            
            for i, slide_file in enumerate(slide_files, 1):
                xml_content = z.read(slide_file)
                tree = ET.fromstring(xml_content)
                texts = []
                for node in tree.iter():
                    if node.tag.endswith('}t'):
                        if node.text:
                            texts.append(node.text)
                print(f"--- Slide {i} ---")
                print(" ".join(texts))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract_text_from_pptx(sys.argv[1])
