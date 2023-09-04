/**-----------------------------------------------------------------------------
 * Variable Resolver
 *
 * Resolves variables in a string with respect to a workspace or file
 *
 * Based on code from:
 * - https://github.com/microsoft/vscode/blob/9450b5e5fb04f2a180cfffc4d27f52f972b1f369/src/vs/workbench/services/configurationResolver/common/variableResolver.ts
 * - https://github.com/microsoft/vscode/blob/9f1aa3c9feecd04a79d22fd6752ba14a83b48f1b/src/vs/workbench/services/configurationResolver/browser/configurationResolverService.ts
 *----------------------------------------------------------------------------*/
import * as vscode from 'vscode';
/** Get file name without extension */
export declare function fileBasenameNoExtension(uri: vscode.Uri): string;
/** Resolves variables formatted like `${VAR_NAME}` within a string */
export declare class VariableResolver {
    private static readonly VARIABLE_REGEXP;
    private static readonly VERSION_FORMAT;
    private readonly _variables;
    private readonly _defaultPattern;
    private readonly _isWindows;
    constructor();
    /** Resolve variables in string given a file URI */
    resolveString(pattern: string | undefined, resource: vscode.Uri, exportExtension?: string): Promise<string>;
    /** Tests all variables */
    testVars(resource: vscode.Uri): void;
    /** Evaluate a single variable in format '${VAR_NAME}'
     *
     * See also: https://code.visualstudio.com/docs/editor/variables-reference
     */
    private evaluateSingleVariable;
    /** Evaluate version number in format '${#}' */
    private getVersionNumber;
    get defaultPattern(): string;
}
