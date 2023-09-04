/**-----------------------------------------------------------------------------
 * Cheatsheet
 *
 * Generates a webview panel containing the OpenSCAD cheatsheet
 *----------------------------------------------------------------------------*/
import * as vscode from 'vscode';
/**
 * OpenSCAD Cheatsheet webview and commands.
 *
 * Only one instance of cheatsheet panel is allowed, so most things are delcared
 * `static`.
 */
export declare class Cheatsheet {
    static readonly csCommandId = "openscad.cheatsheet";
    static readonly viewType = "cheatsheet";
    static currentPanel: Cheatsheet | undefined;
    private static csStatusBarItem;
    private readonly _panel;
    private static config;
    private cheatsheetContent;
    private _disposables;
    /** Create or show cheatsheet panel */
    static createOrShowPanel(extensionPath: vscode.Uri): void;
    /** Recreate panel in case vscode restarts */
    static revive(panel: vscode.WebviewPanel, extensionPath: vscode.Uri): void;
    /** Create a new Cheatsheet */
    private constructor();
    /** Dispose of panel and clean up resources */
    dispose(): void;
    /** Initializes the status bar (if not yet) and return the status bar */
    static getStatusBarItem(): vscode.StatusBarItem;
    /** Dispose of status bar */
    static disposeStatusBar(): void;
    static updateStatusBar(): void;
    /** Run on change active text editor */
    static onDidChangeActiveTextEditor(): void;
    /** Run when configurations are changed */
    static onDidChangeConfiguration(config: vscode.WorkspaceConfiguration): void;
    /** Updates webview html content */
    updateWebviewContent(): void;
    /** True if there at least one open document of languageId `scad`? */
    private static isAnyOpenDocumentScad;
    /** True if a document languageId is `scad` */
    private static isDocumentScad;
}
