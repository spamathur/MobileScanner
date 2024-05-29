# Mobile Scanner

Given a JPEG image, the program finds the edges of the document or receipt and displays a scanned version with OpenCv. The program also automatically creates a PDF file with the same name as the JPEG image with the scanned document. Utilizes the Open CV library.

## To run the program
In the terminal, run the command when in the source directory, 


"python docscanner.py --image {REPLACE WITH THE NAME OF THE JPEG FILE}"


Ex: python docscanner.py --image tommy.jpg


Note: The JPEG file must be in the same directory and the PDF file will be created in the same directory


Note: Will run on Python 3+ and OpenCV 3+
