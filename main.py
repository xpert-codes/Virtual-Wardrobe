import tkinter as tk
from PIL import ImageTk, Image
import os

class ImageGallery(tk.Tk):
    def __init__(self, image_folder_1, image_folder_2):
        tk.Tk.__init__(self)
        self.title("Virtual Wardrobe")
        self.geometry("400x600")
        self.image_folder_1 = image_folder_1
        self.image_folder_2 = image_folder_2
        self.images_1 = []
        self.images_2 = []
        self.current_image_index_1 = 0
        self.current_image_index_2 = 0

        # Load images from the folders
        self.load_images()

        # Create the frame for the first image and button
        frame_1 = tk.Frame(self)
        frame_1.pack(pady=10)

        # Create the image label for the first image
        self.image_label_1 = tk.Label(frame_1)
        self.image_label_1.pack()

        # Create the frame for the first image buttons
        button_frame_1 = tk.Frame(self)
        button_frame_1.pack(pady=5)

        # Create the previous and next buttons for the first image
        previous_button_1 = tk.Button(button_frame_1, text="Previous", command=self.previous_image_1)
        previous_button_1.pack(side=tk.LEFT)
        next_button_1 = tk.Button(button_frame_1, text="Next", command=self.next_image_1)
        next_button_1.pack(side=tk.LEFT)

        # Create the frame for the second image and button
        frame_2 = tk.Frame(self)
        frame_2.pack(pady=10)

        # Create the image label for the second image
        self.image_label_2 = tk.Label(frame_2)
        self.image_label_2.pack()

        # Create the frame for the second image buttons
        button_frame_2 = tk.Frame(self)
        button_frame_2.pack(pady=5)

        # Create the previous and next buttons for the second image
        previous_button_2 = tk.Button(button_frame_2, text="Previous", command=self.previous_image_2)
        previous_button_2.pack(side=tk.LEFT)
        next_button_2 = tk.Button(button_frame_2, text="Next", command=self.next_image_2)
        next_button_2.pack(side=tk.LEFT)

        # Create the button for combining upper and lower images
        combine_button = tk.Button(self, text="Combine & Dress Up", command=self.combine_images)
        combine_button.pack(pady=10)

        # Display the initial images
        self.display_image_1()
        self.display_image_2()

    def load_images(self):
        # Get the list of image files in the first folder
        image_files_1 = [file for file in os.listdir(self.image_folder_1) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Load the images from the first folder using PIL and store them in a list
        for file in image_files_1:
            image_path = os.path.join(self.image_folder_1, file)
            image = Image.open(image_path)
            self.images_1.append(image)

        # Get the list of image files in the second folder
        image_files_2 = [file for file in os.listdir(self.image_folder_2) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Load the images from the second folder using PIL and store them in a list
        for file in image_files_2:
            image_path = os.path.join(self.image_folder_2, file)
            image = Image.open(image_path)
            self.images_2.append(image)

    def display_image_1(self):
        # Get the current image for the first image label
        current_image_1 = self.images_1[self.current_image_index_1]

        # Resize the image to fit the window
        resized_image_1 = current_image_1.resize((200, 200))

        # Convert the image to Tkinter format
        tk_image_1 = ImageTk.PhotoImage(resized_image_1)

        # Update the image label for the first image
        self.image_label_1.config(image=tk_image_1)
        self.image_label_1.image = tk_image_1

    def display_image_2(self):
        # Get the current image for the second image label
        current_image_2 = self.images_2[self.current_image_index_2]

        # Resize the image to fit the window
        resized_image_2 = current_image_2.resize((200, 200))

        # Convert the image to Tkinter format
        tk_image_2 = ImageTk.PhotoImage(resized_image_2)

        # Update the image label for the second image
        self.image_label_2.config(image=tk_image_2)
        self.image_label_2.image = tk_image_2

    def previous_image_1(self):
        # Decrement the current image index for the first image
        self.current_image_index_1 -= 1

        # Wrap around to the last image if index goes below 0
        if self.current_image_index_1 < 0:
            self.current_image_index_1 = len(self.images_1) - 1

        # Display the new image for the first image label
        self.display_image_1()

    def next_image_1(self):
        # Increment the current image index for the first image
        self.current_image_index_1 += 1

        # Wrap around to the first image if index exceeds the number of images
        if self.current_image_index_1 >= len(self.images_1):
            self.current_image_index_1 = 0

        # Display the new image for the first image label
        self.display_image_1()

    def previous_image_2(self):
        # Decrement the current image index for the second image
        self.current_image_index_2 -= 1

        # Wrap around to the last image if index goes below 0
        if self.current_image_index_2 < 0:
            self.current_image_index_2 = len(self.images_2) - 1

        # Display the new image for the second image label
        self.display_image_2()

    def next_image_2(self):
        # Increment the current image index for the second image
        self.current_image_index_2 += 1

        # Wrap around to the first image if index exceeds the number of images
        if self.current_image_index_2 >= len(self.images_2):
            self.current_image_index_2 = 0

        # Display the new image for the second image label
        self.display_image_2()

    def combine_images(self):
        # Get the selected upper and lower images
        selected_upper = self.images_1[self.current_image_index_1]
        selected_lower = self.images_2[self.current_image_index_2]

        # Resize the images to fit the combined image
        resized_upper = selected_upper.resize((200, 200))
        resized_lower = selected_lower.resize((200, 200))

        # Create a new blank image to combine the upper and lower images
        combined_image = Image.new('RGB', (200, 400))

        # Paste the upper and lower images onto the combined image
        combined_image.paste(resized_upper, (0, 0))
        combined_image.paste(resized_lower, (0, 200))

        # Show the combined image
        combined_image.show()


# Create an instance of the ImageGallery class and run the program
image_folder_1 = "Uppers"  # Replace with the path to your first image folder
image_folder_2 = "Lowers"  # Replace with the path to your second image folder
app = ImageGallery(image_folder_1, image_folder_2)
app.mainloop()
