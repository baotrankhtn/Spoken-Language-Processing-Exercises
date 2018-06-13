fprintf('------------------ TRAINING ----------------\n');

% Constants used for 'training.m' & 'test.m'
NUMBER_OF_SPEAKERS = 65;
NUMBER_OF_TESTS_PER_SPEAKER = 20;

% Calculate GMM for each speaker
for i = 1: NUMBER_OF_SPEAKERS
    % Generate speaker position string
    if i < 10
        strSpeakerPosition = strcat('0',num2str(i));
    else
        strSpeakerPosition = num2str(i);
    end
    
    fprintf('- Processing speaker %s\n', strSpeakerPosition);
    
    % wav -> MFCC
    % File path example: data/01/training/01.wav
    audioTrain = audioread(strcat('data/', strSpeakerPosition, '/train/01.wav'));
    mfccTrain = mfcc(audioTrain);

    % Training 
    g0 = gNew(12, 16, 'diag');
    g1 = gInit(g0, mfccTrain, 100);
    g2 = gRE(g1, mfccTrain, 100);
    arrayGMM(i) = g2;
end



