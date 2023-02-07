class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        remainingWidth = maxWidth
        wordsInLine = []
        
        for i in range(len(words)):
            word = words[i]
            nextWord = None
            nextWordLength = 0

            if (i+1 < len(words)):
                nextWord = words[i+1]
                nextWordLength = len(nextWord)
            wordLength = len(word)

            if remainingWidth == wordLength:
                wordsInLine.append(word)
                lines.append(' '.join(wordsInLine))
                
                remainingWidth = maxWidth
                wordsInLine = []
            elif remainingWidth > wordLength:
                wordsInLine.append(word)
                remainingWidth -= wordLength + 1
           
            if (remainingWidth < nextWordLength or nextWord is None):
                
                if len(wordsInLine) > 1 and nextWord is not None:
                    wordInLineIdx = 0
                    
                    while remainingWidth > -1:
                        wordInLine = wordsInLine[wordInLineIdx]
                        wordInLine += ' ' 
                        wordsInLine[wordInLineIdx] = wordInLine
                        
                        if (wordInLineIdx < len(wordsInLine) - 2):
                            wordInLineIdx += 1
                        else:
                            wordInLineIdx = 0
                        remainingWidth -= 1
                  
                    lines.append(' '.join(wordsInLine))
                elif len(wordsInLine) == 1:
                    line = wordsInLine[0] + ' '
                    while remainingWidth > 0:
                        line += ' '
                        remainingWidth -= 1
                    lines.append(line)
                elif len(wordsInLine) > 1 and nextWord is None:
                    line = ' '.join(wordsInLine)
                    while remainingWidth > -1:
                        line += ' '
                        remainingWidth -= 1
                    lines.append(line)

                remainingWidth = maxWidth
                wordsInLine = []
        return lines