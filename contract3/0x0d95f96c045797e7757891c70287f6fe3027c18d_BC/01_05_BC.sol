// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

/// @title: The Canada Collection
/// @author: manifold.xyz

import "./02_05_ERC721Creator.sol";

///////////////////////////////////////////////////////////////////////////////////////
//                                                                                   //
//                                                                                   //
//              /\                                                                   //
//             /**\                                                                  //
//            /****\   /\                                                            //
//           /      \ /**\                                                           //
//          /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\        //
//         /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \       //
//        /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \      //
//       /  /      \/  \/\   \  /      \    /   /    \                SEB            //
//    __/__/_______/___/__\___\__________________________________________________    //
//                                                                                   //
//                                                                                   //
///////////////////////////////////////////////////////////////////////////////////////


contract BC is ERC721Creator {
    constructor() ERC721Creator("The Canada Collection", "BC") {}
}