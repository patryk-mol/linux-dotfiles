/**
 * Cheatsheet styles
 */
import * as vscode from 'vscode';
/**
 * Available css styles for Cheatsheet. Paths are relative to [extensionUri].
 */
export declare const STYLES: {
    auto: string;
    original: string;
};
type StyleKey = keyof typeof STYLES;
/** Default style */
export declare const DEFAULT_STYLE: StyleKey;
export declare class CheatsheetStyles {
    readonly styles: {
        [key in StyleKey]: vscode.Uri;
    };
    readonly defaultStyle: vscode.Uri;
    [Symbol.iterator](): Iterator<StyleKey>;
    constructor(stylesUri: vscode.Uri);
}
export {};
