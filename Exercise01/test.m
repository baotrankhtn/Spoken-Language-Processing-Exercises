fprintf('------------------ TESTING ----------------');
for i = 1: NUMBER_OF_SPEAKERS
    % Generate speaker position string
    if i < 10
        strSpeakerPosition = strcat('0', num2str(i));
    else
        strSpeakerPosition = num2str(i);
    end
    
    fprintf('\n\n- Processing speaker %s', strSpeakerPosition);
    
    % Loop all tests of each speaker: 20 files
    numberOfPass = 0;
    for j = 1: NUMBER_OF_TESTS_PER_SPEAKER
        % Generate test position string
        if j < 10
            strTestPosition = strcat('0',num2str(j));
        else
            strTestPosition = num2str(j);
        end
        
        fprintf('\n+ Test %s: ', strTestPosition);
        
        % Calculate MFCC
        audioTest = audioread(strcat('data/', strSpeakerPosition, '/test/', strTestPosition, '.wav'));
        mfccTest = mfcc(audioTest);
        
        % P
        for k = 1 : NUMBER_OF_SPEAKERS
            arrayP(k) = mean(gPr(arrayGMM(k), mfccTest));
        end
        
        % Find max p
        posMax = 1;
        for l = 2 : NUMBER_OF_SPEAKERS
            if arrayP(l) > arrayP(posMax)
                posMax = l;
            end
        end
        
        % Check if test is failed
        if posMax == i
            fprintf('Pass');
            numberOfPass = numberOfPass + 1;
        else
            fprintf('Fail');
        end
    end
    
    % Pass/Fail
    percentPass = numberOfPass * 100 / NUMBER_OF_TESTS_PER_SPEAKER;
    percentFail = 100 - percentPass;
    fprintf('\n=> Pass:  %d%%, Fail: %d%%', percentPass, percentFail);
end