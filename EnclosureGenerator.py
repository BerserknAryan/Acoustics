import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class EnclosurePanelGenerator:
    def __init__(self, length, width, height):
        self.length1 = length1
        self.length2 = length2
        self.width1 = width1
        self.width2 = width2
        self.heigh1 = height1
        self.height2 = height2
        self.
        self.panels = []

    def generate_panels(self):
        # Define vertices for the enclosure
        vertices = np.array([[0, 0, 0],
                             [self.length, 0, 0],
                             [self.length, self.width, 0],
                             [0, self.width, 0],
                             [0, 0, self.height],
                             [self.length, 0, self.height],
                             [self.length, self.width, self.height],
                             [0, self.width, self.height]])

        # Define panel faces and labels
        faces_labels = [
            ('Front', [vertices[j] for j in [0, 1, 2, 3]]),
            ('Back', [vertices[j] for j in [4, 5, 6, 7]]),
            ('Top', [vertices[j] for j in [0, 3, 7, 4]]),
            ('Bottom', [vertices[j] for j in [1, 2, 6, 5]]),
            ('Left', [vertices[j] for j in [0, 1, 5, 4]]),
            ('Right', [vertices[j] for j in [2, 3, 7, 6]])
        ]

        # Add panel faces to the list
        for label, face in faces_labels:
            self.panels.append({'label': label, 'face': face, 'edge': None, 'type': 'normal'})

        return self.panels

    def plot_enclosure(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot enclosure panels
        for panel in self.panels:
            ax.add_collection3d(Poly3DCollection([panel['face']], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

            # Add label to the center of each face
            face_center = np.mean(panel['face'], axis=0)
            ax.text(face_center[0], face_center[1], face_center[2], panel['label'], color='black', fontsize=8)

        # Set axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    def create_baffle_board(self, speaker_cutout_dimensions):
        # Create a baffle board with speaker cutouts
        baffle_board = np.array([[0, 0, 0],
                                 [self.length, 0, 0],
                                 [self.length, self.width, 0],
                                 [0, self.width, 0]])

        # Add cutouts
        for cutout_dim in speaker_cutout_dimensions:
            cutout_vertices = np.array([[cutout_dim[0], cutout_dim[1], 0],
                                        [cutout_dim[2], cutout_dim[1], 0],
                                        [cutout_dim[2], cutout_dim[3], 0],
                                        [cutout_dim[0], cutout_dim[3], 0]])
            baffle_board = np.concatenate((baffle_board, cutout_vertices), axis=0)

        # Add baffle board to the list
        self.panels.append({'label': 'Baffle', 'face': [baffle_board[j] for j in [0, 1, 2, 3]], 'edge': None, 'type': 'baffle'})

        return baffle_board

    def create_internal_board(self, label, position):
        # Create an internal board with a labeling system
        internal_board = np.array([[0, 0, 0],
                                   [self.length, 0, 0],
                                   [self.length, self.width, 0],
                                   [0, self.width, 0]])

        # Shift the internal board to the specified position
        internal_board += np.array([position[0], position[1], position[2]])

        # Add internal board to the list
        self.panels.append({'label': label, 'face': [internal_board[j] for j in [0, 1, 2, 3]], 'edge': None, 'type': 'internal'})

        # Add labels
        label_position = [position[0] + self.length / 2, position[1] + self.width / 2, position[2]]
        plt.text(label_position[0], label_position[1], label_position[2], label, color='black', fontsize=8)

        return internal_board

    def connect_panels(self, panel1_label, panel2_label, face1, face2, edge1, edge2):
        # Connect two panels based on their labels, faces, and edges
        panel1 = next(panel for panel in self.panels if panel['label'] == panel1_label)
        panel2 = next(panel for panel in self.panels if panel['label'] == panel2_label)

        panel1['edge'] = edge1
        panel2['edge'] = edge2

        # Example: Connecting the panels by modifying vertices
        panel1['face'][face1] = panel2['face'][face2]
        panel2['face'][face2] = panel1['face'][face1]

