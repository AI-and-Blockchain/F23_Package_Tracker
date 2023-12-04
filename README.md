<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![Activity][activity-shield]][activity-url]
<!-- [![Stargazers][stars-shield]][stars-url] -->
Chase Grajeda (grajec)

Jianye Peng (pengj6)

Eddie Poon (poone)

Aneesh Kolukuluri(koluka)

<!-- TABLE OF CONTENTS -->
<details>
    <summary> Table of Contents </summary>
    <ol>
        <li>
            <a href="#about"> About the project</a>
            <ul>
                <li><a href="#built-with">Built With</a>
            </ul>
        </li>
        <li>
            <a href="#prerequisites"> Prerequisites</a>
        </li>
        <li>
            <a href="#blockchain"> Blockchain Component</a>
        </li>
        <li>
            <a href="#diagrams"> Diagrams</a>
        </li>
        <li>
            <a href="#license"> License</a>
        </li>
    </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About
<div align="center">
<h3 align="center">Package Tracker</h3>
<p>
The Package Tracker introduces faster and safer standards of delivery for cities and local populations. Users may sign up to deliver for us, from which they’ll receive instant payment for successful delivery. Packages are brought from a distribution center and delivered to a local parcel locker. Each package has a unique identifier to be scanned in at each point of the process. Receiving users are given real-time updates on the status of their package, as well as optimized route planning. 

</P>
</div>

### Built With

* [![Remix][Remix]][Remix-url]
* [![Pytorch][Pytorch]][Pytorch-url]
* [![Chainlink][Chainlink]][Chainlink-url]


<!-- Getting Started -->
## Prerequisites
 * Clone or fork the repo
    * GitHub Desktop: download [here](https://desktop.github.com/)
    * Clone repo through Git Bash
    ```sh
    $ git clone https://github.com/AI-and-Blockchain/F23_Package_Tracker
    ```
    * To fork, press the fork button on the top right of the repo, or [here](https://github.com/AI-and-Blockchain/F23_Package_Tracker/fork)
 * Install Applications
    * Node.js: download [here](https://nodejs.org/en)
    * Ganache: downlaod [here](https://trufflesuite.com/ganache/)
 * Install All Requirements 
    * Download through the command line
    ```sh
    $ pip install -r requirements.txt
    ```
    ```sh
    $ npm install
    ```
## Setting up the webpage and API
 * Do the instructions in this order
 * Open Ganache
    * Press Quickstart if it is the first time, otherwise choose a already created workspace
 * Click the key icon on any of the Addresses on the right side of the screen
    * In contractToPy.py, towards the top of the file, change the address and private key to the ones shown in ganache and save the file
 * Run the API
    * Run the command in the terminal
    ```sh
    $ uvicorn contractToPy:app --reload
    ```
 * Open a new terminal and change directories
    * Run the command in the terminal
    ```sh
    $ cd Webpage/web-page
    ```
    * Run npm
    ```sh
    npm start
    ```

## Demo Video
https://www.youtube.com/watch?v=HKp4oUxC0eo

## Blockchain Component

<p>
QR code creation: We will be required to generate three separate QR codes to call different functions of the smart contract in order to facilitate communication and delivery of information between the three parties: sender, receiver, and courier.

The generation of the QR codes can be done using the following plug-in: https://github.com/jibrelnetwork/ethereum-qr-code/blob/master/README.md

Functions to update state variables, and send status updates such as expected ETA will be created so that the receiver can be aware of the current status of the delivery.

Events can be used to create a log and keep track of the various steps involved from start to finish.
</P>

## Diagrams

### Architecture Diagram
![image](Assets/Components.png)

### Sequence Diagram
![image](Assets/sequencediagram.png)

### Flowchart
![image](Assets/Flowchart.png)

## License

Distributed under the Apache License. See [LICENSE](https://github.com/AI-and-Blockchain/F23_Package_Tracker/blob/main/LICENSE) for more information.

<!-- https://home.aveek.io/GitHub-Profile-Badges/ -->

<!-- LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/AI-and-Blockchain/F23_Package_Tracker.svg?style=for-the-badge
[contributors-url]: https://github.com/AI-and-Blockchain/F23_Package_Tracker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AI-and-Blockchain/F23_Package_Tracker.svg?style=for-the-badge
[forks-url]: https://github.com/AI-and-Blockchain/F23_Package_Tracker/network/members
[stars-shield]: https://img.shields.io/github/stars/AI-and-Blockchain/F23_Package_Tracker.svg?style=for-the-badge
[stars-url]: https://github.com/AI-and-Blockchain/F23_Package_Tracker/stargazers
[issues-shield]: https://img.shields.io/github/issues/AI-and-Blockchain/F23_Package_Tracker.svg?style=for-the-badge
[issues-url]:  https://github.com/AI-and-Blockchain/F23_Package_Tracker/issues
[license-shield]: https://img.shields.io/github/license/AI-and-Blockchain/F23_Package_Tracker.svg?style=for-the-badge
[license-url]: https://github.com/AI-and-Blockchain/F23_Package_Tracker/blob/master/LICENSE.txt

[activity-shield]: https://img.shields.io/github/last-commit/AI-and-Blockchain/F23_Package_Tracker?style=for-the-badge
[activity-url]: https://github.com/Zxhjlk/Accessible-Routes/activity



[Remix]: https://img.shields.io/badge/Remix-000000.svg?style=for-the-badge&logo=Remix&logoColor=white
[Remix-url]: https://remix.ethereum.org/

[Pytorch]: https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[Pytorch-url]: https://pytorch.org/

[Chainlink]: https://img.shields.io/badge/Chainlink-375BD2.svg?style=for-the-badge&logo=Chainlink&logoColor=white
[Chainlink-url]: https://chain.link/
