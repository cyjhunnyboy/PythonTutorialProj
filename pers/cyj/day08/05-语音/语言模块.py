from win32com.client import constants
import os
import win32com.client
import pythoncom


class SpeechRecognition:

    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammer = self.context.CreateGrammer()
        self.grammer.DictationSetState(0)
        self.wordsRule = self.grammer.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammer.Rules.Commit()
        self.grammer.CmdSetRuleState("wordsRule", 1)
        self.grammer.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")

    def say(self, phrase):
        self.speaker.Speak(phrase)


class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):

    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：", newResult.PhraseInfo.GetText())


if __name__ == "__main__":
    wordsToAdd = ["关机", "取消关机", "记事本", "画图版", "写字板", "设置", "关闭记事本"]
    speachReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
