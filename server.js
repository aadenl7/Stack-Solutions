const express = require('express');
const { execFile } = require('child_process'); 
const path = require('path'); 

const app = express();

app.use(express.static('public'));
app.use(express.json()); 
app.use(express.urlencoded({ extended: true }));

app.post('/run-quiz', (req, res) => {
    const userAnswers = req.body.answers;

    if (!userAnswers || userAnswers.length !== 5) {
        return res.status(400).send("Invalid input: Please provide 5 quiz answers.");
    }
    
    console.log("Received answers:", userAnswers);

    const pythonExecutable = 'python'; 
    const pythonScript = path.join(__dirname, 'quiz.py');
    const inputData = JSON.stringify(userAnswers);

    // Launch the Python script
    const pythonProcess = execFile(pythonExecutable, [pythonScript], (execError, standardOutput, standardError) => {
        if (execError || standardError) {
            console.error("Python Execution Failure:", execError || standardError);
            
            // Check for common error (Python not found)
            if (execError && execError.code === 'ENOENT') {
                 return res.status(500).send("FATAL Error: Python executable not found. Check your system PATH.");
            }
            
            // Send back the detailed error output for debugging
            const errorMessage = standardError || execError.message;
            return res.status(500).send(`Python Script Execution Error:\n${errorMessage}\n\nCaptured Output: ${standardOutput}`);
        }

        // If successful, send the output back to the client
        return res.send(standardOutput);
    });
    

    pythonProcess.stdin.write(inputData + '\n');
    pythonProcess.stdin.end();
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));