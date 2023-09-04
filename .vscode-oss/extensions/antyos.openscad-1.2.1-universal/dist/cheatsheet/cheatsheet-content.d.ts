import { HTMLElement } from 'node-html-parser';
import * as vscode from 'vscode';
/** Get HTML content of the OpenSCAD cheatsheet */
export declare class CheatsheetContent {
    /** Uri to the directory containing the cheatsheet html and style sheets */
    private readonly _cheatsheetUri;
    /** HTMLElement of document */
    private _document?;
    /** The last key used to get the cheatsheet stylesheet */
    private _lastStyleKey?;
    /** Styles container */
    private _cheatsheetStyles;
    /** Content Security Policy */
    private _csp;
    private _webview;
    constructor(cheatsheetUri: vscode.Uri, webview: vscode.Webview);
    /** Get cheatsheet HTML content. Stores HTML from lastStyleKey. */
    getContent(styleKey: string): Promise<string>;
    /**
     * Disable all stylesheet links in `this._document`.
     * Returns false if `this._document` is undefined.
     */
    disableAllStylesheets(): boolean;
    /**
     * Enable a stylesheet link by id from `this._document`.
     * Returns false if `this._document` is undefined or no stylesheet exists
     * with the passed id.
     */
    enableStylesheet(id: string): boolean;
    setStylesheet(id: string): boolean;
    /** The key used the last time getContent() was called */
    get lastStyleKey(): string | undefined;
    /**
     * Get a <link> HTMLElement for a stylesheet.
     * @param {string} href Reference to stylesheet
     * @param {string | undefined} id of element
     * @returns HTMLElement
     */
    private getStyleSheetElement;
    /**
     * Get a Content-Security-Policy element for the webview
     *
     * See:
     *  - https://code.visualstudio.com/api/extension-guides/webview#content-security-policy
     *  - https://developers.google.com/web/fundamentals/security/csp/
     */
    protected getCSPElement(): HTMLElement;
    /** Get the cheatsheet html content for webview */
    private getCheatsheetHTML;
}
