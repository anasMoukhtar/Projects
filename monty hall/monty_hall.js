const readline = require("readline");

// Create an interface for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function montyHall(rounds, switchChoice) {
    let wins = 0;
    let losses = 0;
    let completedRounds = 0;

    const batchSize = 1000000; // Process in batches of 1 million
    const totalBatches = Math.ceil(rounds / batchSize);

    console.log(`Starting simulation of ${rounds.toLocaleString()} rounds...`);

    for (let batch = 0; batch < totalBatches; batch++) {
        const currentBatchSize = Math.min(batchSize, rounds - completedRounds);

        for (let i = 0; i < currentBatchSize; i++) {
            // Step 1: Randomly place the car behind one of the doors
            const carPosition = Math.floor(Math.random() * 3);

            // Step 2: Randomly select a door
            let userChoice = Math.floor(Math.random() * 3);

            // Step 3: Reveal a wrong door
            const possibleReveals = [0, 1, 2].filter(
                (door) => door !== userChoice && door !== carPosition
            );
            const revealedDoor = possibleReveals[Math.floor(Math.random() * possibleReveals.length)];

            // Step 4: If switching, change the user's choice
            if (switchChoice) {
                userChoice = [0, 1, 2].find(
                    (door) => door !== userChoice && door !== revealedDoor
                );
            }

            // Step 5: Check if the user wins
            if (userChoice === carPosition) {
                wins++;
            } else {
                losses++;
            }
        }

        completedRounds += currentBatchSize;

        // Log progress after each batch
        console.log(`${completedRounds.toLocaleString()} rounds completed...`);
    }

    // Output final results
    console.log(`Simulation completed.`);
    console.log(`Rounds Played: ${rounds.toLocaleString()}`);
    console.log(`Wins: ${wins.toLocaleString()}`);
    console.log(`Losses: ${losses.toLocaleString()}`);
    console.log(`Win Rate: ${(wins / rounds * 100).toFixed(6)}%`);
}

// Prompt user for inputs
rl.question("How many rounds would you like to play? ", (roundsInput) => {
    const rounds = parseInt(roundsInput);

    rl.question("Do you want to switch your choice every time? (yes/no) ", (switchInput) => {
        const switchChoice = switchInput.toLowerCase() === "yes";

        console.time("MontyHall Simulation");
        montyHall(rounds, switchChoice);
        console.timeEnd("MontyHall Simulation");

        rl.close();
    });
});
